module Main (main) where

import Advent (getInput)
import Data.List (sort, group)

main :: IO ()

main =
  do input <- parseInput <$> getInput 2
     print (part1 input)

parseInput :: String -> [String]
parseInput = lines

part1 :: [String] -> Int
part1 s = (sum $ map (fromEnum . (hasExactlyN 2)) s) * (sum $ map (fromEnum . (hasExactlyN 3)) s)

getLetterCounts :: String -> [Int]
getLetterCounts = map length . group . sort

hasExactlyN :: Int -> String -> Bool
hasExactlyN n s = elem n $ getLetterCounts s