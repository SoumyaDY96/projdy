#!/bin/bash
groupadd -r prometheus
useradd -s /sbin/nologin -r -g prometheus prometheus

apt update -y


if [ ! $(dpkg-query -s wget | grep -ie 'ok installed') ]; then
  apt install wget -y
fi

mkdir /etc/prometheus
mkdir /var/lib/prometheus

wget https://github.com/prometheus/prometheus/releases/download/v2.47.0-rc.0/prometheus-2.47.0-rc.0.linux-amd64.tar.gz

tar -xzvf prometheus-2.47.0-rc.0.linux-amd64.tar.gz

mv prometheus-2.47.0-rc.0.linux-amd64 prometheus

mv prometheus/prometheus.yml /etc/prometheus/
mv prometheus/console_libraries/ /etc/prometheus
mv prometheus/consoles/ /etc/prometheus

chown -R prometheus:prometheus /etc/prometheus
chown -R prometheus:prometheus /etc/prometheus/console_libraries/ 
chown -R prometheus:prometheus /etc/prometheus/consoles/
chown -R prometheus:prometheus /var/lib/prometheus 

mv prometheus/promtool /usr/local/bin
mv prometheus/prometheus /usr/local/bin

chown prometheus:prometheus /usr/local/bin/prometheus
chown prometheus:prometheus /usr/local/bin/promtool

iptables -I INPUT -p tcp --dport 9090 -j ACCEPT
iptables-save

cat <<EOF > /etc/systemd/system/prometheus.service
 [Unit]
 Description=Prometheus
 Wants=network-online.target
 After=network-online.target
 
 [Service]
 User=prometheus
 Group=prometheus
 Type=simple
 ExecStart=/usr/local/bin/prometheus \
     --config.file /etc/prometheus/prometheus.yml \
     --storage.tsdb.path /var/lib/prometheus/ \
     --web.console.templates=/etc/prometheus/consoles \
     --web.console.libraries=/etc/prometheus/console_libraries
 
[Install]
WantedBy=multi-user.target
EOF

systemctl start prometheus
systemctl enable prometheus
systemctl list-units | grep -ie prometheus