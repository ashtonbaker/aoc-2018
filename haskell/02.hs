module Problem02 (solve02) where

import Advent (getInput)
import Data.List

solve02 :: IO ()

solve02 =
  do input <- parseInput <$> getInput 2
     print (part1 input)
     print (part2 input)

parseInput :: String -> [String]
parseInput = lines

part1 :: [String] -> Int
part1 s = (getStringsWithN 2 s) * (getStringsWithN 3 s)

part2 :: [String] -> String
part2 list =  uncurry intersect $ head [pair | pair <- pairs list, (uncurry distance $ pair) == 1]

getLetterCounts :: String -> [Int]
getLetterCounts = map length . group . sort

hasExactlyN :: Int -> String -> Bool
hasExactlyN n s = elem n $ getLetterCounts s

getStringsWithN :: Int -> [String] -> Int
getStringsWithN n s = sum $ map (fromEnum . (hasExactlyN n)) s

distance :: Eq a => [a] -> [a] -> Int
distance s1 s2 = sum . map fromEnum $ zipWith (/=) s1 s2

pairs :: [a] -> [(a, a)]
pairs l = [(x,y) | (x:ys) <- tails l, y <- ys]
