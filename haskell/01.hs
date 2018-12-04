module Main (main) where

import Advent (getInput)
import Data.List.Utils (replace)
import Data.Set (Set)

main :: IO ()

main =
  do input <- parseInput <$> getInput 1
     print (part1 input)
     print (part2 input)

parseInput :: String -> [Int]
parseInput = map read . map (replace "+" "") . lines

part1 :: [Int] -> Int
part1 = sum

part2 :: [Int] -> [Int]
part2 = take 100 . scanl1 (+) . cycle

repeats :: [Int] -> [Int]
