//{ Driver Code Starts
//Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();
});

function readLine() {
    return inputString[currentLine++];
}

function printList(res,n){
    let s="";
    for(let i=0;i<n;i++){
        s+=res[i];
        s+=" ";
    }
    console.log(s);
}


function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let a = new Array(n);
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++){
            a[i] = input_ar1[i];
        }
        let obj = new Solution();
        let res = obj.minCandy(n, a);
        console.log(res);
        
    }
}// } Driver Code Ends



// } Driver Code Ends


//User function Template for javascript
/**
 * @param {number} N
 * @param {number[]} ratings
 * @returns {number}
*/

class Solution {
    //Function to find minimum number of candies to be distributed among the students.
      minCandy(N, ratings){
        //your code here
        /*
        let us consider, all the candidates get atleast 1 candy.
        so create a list 'sm' filled with value 1.
        'sm' will hold the number of possession of candies for each student.
        */
        let sm=Array(N).fill(1);
        
        
        /* 
        create an iteration from left to right 
        from 1st index to last index i.e. not from 0th index, 
        to check if ranking of current student is greater than its' 
        previous student. 
        
        if it is true then increase the number of possession of candies 
        for current student by 1 with respect to candies own by previous student
        */

        for(let i=1;i<N;i++){
            if (ratings[i]>ratings[i-1]){
                sm[i]=sm[i-1]+1;
            }    
            
        }

        /* 
        similarly create an iteration from right to left  
        from one index before last index, to 0th index, 
        to check if ranking of current student is greater than its' 
        next student. 
        
        if it is true then increase the number of possession of candies 
        for current student by 1 with respect to candies own by previous student
        */

        for(let i=N-2;i>=0;i--){
            if ((ratings[i]>ratings[i+1]) && (sm[i]<=sm[i+1])){
                sm[i]=sm[i+1]+1;
            }
        }
        
        /*
        now return the sum of array 'sm' which holds the 
        numbers of possession of candies for
        every student
        */

        let totalCandies = sm.reduce((a, b) => a + b, 0);
        return totalCandies;
    }
}