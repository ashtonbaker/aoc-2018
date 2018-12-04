module Advent where

import Text.Printf

getInput :: Int -> IO String

getInput i = readFile (printf "../input/%02d.txt" i)