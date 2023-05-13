module Main where

import System.IO
import Data.Char
import Data.Maybe
import Data.List

--Encoded alphabet for cypher
alphabet = [['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z']]

buildKey :: [Int] -> [Char]
--base case
buildKey [] = []
buildKey (x:xs) = (alphabet !! (x-1)) ++ buildKey xs 


generateKey :: [Char]
generateKey = buildKey giveRandomSet

--this is a generated list of random integers from 1-26 inclusive that do not repeat 
--they were produced in java
--the program can be run again for a different set of random numbers
--test cases
--[19,23,12,13,15,26,21,4,17,18,20,8,1,11,24,9,25,10,2,14,16,6,22,3,7,5]
--[23,26,10,3,15,19,12,24,13,1,11,22,21,14,5,25,8,9,17,4,20,18,16,2,7,6]
--[10,13,15,7,18,26,19,5,20,8,17,2,4,25,3,9,14,12,21,11,23,24,16,22,1,6]
--[15,24,4,7,14,6,19,22,26,5,1,3,20,2,25,23,17,18,9,10,12,8,21,11,16,13]
--[9,24,12,13,22,17,20,25,26,6,21,3,23,5,14,18,15,1,8,16,10,2,19,11,4,7]
--[26,18,8,21,6,15,5,1,22,17,14,16,25,9,24,20,19,13,10,2,7,11,4,3,12,23]
--[18,23,21,16,1,2,15,24,11,22,3,6,12,19,26,17,25,13,4,20,10,5,8,7,14,9]
--[21,1,11,25,13,5,2,16,8,22,7,12,4,15,23,26,20,17,9,19,3,10,6,18,14,24]
--[5,20,25,21,10,2,19,8,1,9,11,16,18,23,6,13,12,4,7,17,15,3,26,22,14,24]
giveRandomSet :: [Int]
giveRandomSet = [18,23,21,16,1,2,15,24,11,22,3,6,12,19,26,17,25,13,4,20,10,5,8,7,14,9]

--isInList :: Char -> [Char] -> Bool
--isInList a b = a `elem` b

numToIpAddress :: Int -> [Char]
numToIpAddress x = init (tail (takeOutCommas (show ((binaryToDecimal (fromDigits (giveFirstSegDec (decimalToBinaryFinal (decimalToBinary x)) 0))):[] ++ (binaryToDecimal (fromDigits (giveSecondSegDec (decimalToBinaryFinal (decimalToBinary x)) 0))):[] ++ (binaryToDecimal (fromDigits (reverse (giveSecondSegDec (reverse (decimalToBinaryFinal (decimalToBinary x))) 0)))):[] ++ (binaryToDecimal (fromDigits (reverse (giveFirstSegDec (reverse (decimalToBinaryFinal (decimalToBinary x))) 0)))):[]))))

takeOutCommas:: [Char] -> [Char]
takeOutCommas [] = []
takeOutCommas (x:xs) 
    | (isDigit x) = x : [] ++ (takeOutCommas xs)
    | otherwise = '.':[] ++ takeOutCommas xs

decimalToBinary :: Int -> [Int]
decimalToBinary 0 = []
decimalToBinary n = decimalToBinary (div n 2) ++ [(mod n 2)]

zeroArray :: [Int]
zeroArray = [0]

decimalToBinaryFinal :: [Int] -> [Int]
decimalToBinaryFinal x = zeroArray ++ x

giveFirstSegDec :: [Int] -> Int -> [Int]
giveFirstSegDec [] n = []
giveFirstSegDec (x:xs) n
    | (n < 8) = (x :[]) ++ (giveFirstSegDec xs (n+1))
    | otherwise = [] 

giveSecondSegDec :: [Int] -> Int -> [Int]
giveSecondSegDec [] n = []
giveSecondSegDec (x:xs) n
    | (n > 7)&&(n<16) = x :[] ++ (giveSecondSegDec xs (n+1))
    | otherwise = giveSecondSegDec xs (n+1)

binaryToDecimal :: Integral i => i -> i
binaryToDecimal 0 = 0
binaryToDecimal i = 2 * binaryToDecimal (div i 10) + (mod i 10)

ipAddress :: [Char]
ipAddress = "129.144.50.56"
decimalVal :: Int
decimalVal = 2173710904

ipAddressToNum :: [Char] -> Int
ipAddressToNum ip = ((charToInt (giveFirstSeg ip)) * 16777216) + ((charToInt (giveFirstSeg (giveSecondSeg ip))) * 65536) + ((charToInt (reverse (giveFirstSeg (giveSecondSeg (reverse ip))))) * 256) + ((charToInt (reverse (giveFirstSeg (reverse ip)))) * 1) 

giveFirstSeg :: [Char] -> [Char]
giveFirstSeg [] = []
giveFirstSeg (x:xs) 
    | (isDigit x) = x : [] ++ (giveFirstSeg xs)
    | otherwise = []

giveSecondSeg :: [Char] -> [Char]
giveSecondSeg [] = []
giveSecondSeg (x:xs) 
    | (isDigit x) = giveSecondSeg xs
    | otherwise = xs

--turns a string of integers into an int
charToInt :: [Char] -> Int
charToInt x = read(x)


encrypt :: [Char] -> [Char] -> [Char]
encrypt [] a = []
encrypt (x:xs) (a) = (a !! ((ord (toUpper x)) - 65)) :[] ++ (encrypt xs (a))

decrypt :: [Char] -> [Char] -> [Char]
decrypt [] a = []
decrypt (x:xs) (a) = (alphabet !! (giveIndex x a 0)) ++ decrypt xs a

giveIndex :: Char -> [Char] -> Int -> Int
giveIndex a (x:xs) n 
    | (a == x) = n
    | otherwise = giveIndex a xs (n+1) 

fromDigits = foldl addDigit 0
   where addDigit num d = 10*num + d

--to string 
main :: IO ()
main = do
    putStrLn $ "Generated Key: " ++ show (generateKey)
    putStrLn $ "Word: " ++ show "Shreyan"
    putStrLn $ "Encrypted word: " ++ show (encrypt "Shreyan" generateKey)
    putStrLn $ "Decrypted word: " ++ show (decrypt (encrypt "Shreyan" generateKey) generateKey)
    
    putStrLn $ "IP Address: " ++ show "98.113.85.191"
    putStrLn $ "Decimal of IP Adress: " ++ show (ipAddressToNum "98.113.85.191")
    putStrLn $ "Num to IP Address: " ++ show (numToIpAddress (ipAddressToNum "98.113.85.191"))
    
    





