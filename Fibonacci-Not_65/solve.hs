import Data.Char

g :: Int -> Integer
g 0 = 0
g 1 = 1
g x = (g (x-1) + g (x-2))^2

w :: Int -> Integer
w 0 = 0
w 1 = 1
w x = (w (x-1))^2 + (w (x-2))^2

f :: Int -> Integer
f x = (g x) - (w x)

digits :: Integer -> [Int]
digits = map digitToInt . show

sumDigits :: [Int] -> Int
sumDigits = foldr (+) 0

main = putStrLn . show . sumDigits . digits $ f 30



-- g :: Int -> Integer
-- g = (map gs [0..] !!)
--   where gs 0 = 0
--         gs 1 = 1
--         gs x = (g (x-1) + g (x-2))^2

-- w :: Int -> Integer
-- w = (map ws [0..] !!)
--   where ws 0 = 0
--         ws 1 = 1
--         ws x = (w (x-1))^2 + (w (x-2))^2

-- f :: Int -> Integer
-- f x = (g x) - (w x)

-- sumDigits n = step n 0
--     where step 0 acc = acc
--           step x acc = step (x `div` 10) (acc + (x `mod` 10))

-- main = putStrLn . show . sumDigits $ f 30
