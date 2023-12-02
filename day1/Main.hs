
import System.IO

getFirstDigit :: String -> Int
getLastDigit :: String -> Int

eval :: [String] -> Int

getFirstDigit x = read [x] :: Int
getLastDigit (x:xs) = read [last xs] :: Int

eval x = 



main :: IO ()
main = do
    handle <- openFile "input.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show $ lines contents
    hClose handle