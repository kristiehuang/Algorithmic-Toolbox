package com.kristiehuang.algotoolbox;
import java.util.*;
import java.io.*;

public class MaxPairwiseProduct {
    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }
        
        //CREATING ARRAY SUPER BIG
//        int maxSize = (int) Math.pow(10, 5);
//        int[] numbers = new int[2*maxSize];
//        
//        for(int i = 0; i < 2*maxSize; i++) {
//        		numbers[i] = i+1;
//        }
//      System.out.println(getMaxPairwiseProduct(numbers));

        
        System.out.println(getMaxPairwiseProduct(numbers));
    }
    
    static Long getMaxPairwiseProduct(int[] numbers) {
        Long max_product = (long) 0;
        int n = numbers.length;

		int firstMax = 0;
		int secondMax = 0;

        for (int i = 1; i < n; i++) {
        		//find largest, save index
        		if (numbers[i] > numbers[firstMax]) {
        			firstMax = i;
        		}
        }
        
        if (firstMax == 0) {
        		secondMax = 1;
        }
        for (int i = 0; i < n; i++) {
        		if (i != firstMax) {
            		if (numbers[i] > numbers[secondMax]) {
            			secondMax = i;
            		}
        		}
        }
        
        max_product = ((long) numbers[firstMax]) * ((long) numbers[secondMax]);
        return max_product;
    }

   


    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new
                    InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

}