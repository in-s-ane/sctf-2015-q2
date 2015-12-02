g :: Int -> Integer
g = (map gs [0..] !!)
  where gs 0 = 0
        gs 1 = 1
        gs x = (g (x-1) + g (x-2))^2

w :: Int -> Integer
w = (map ws [0..] !!)
  where ws 0 = 0
        ws 1 = 1
        ws x = (w (x-1))^2 + (w (x-2))^2

f :: Int -> Integer
f x = (g x) - (w x)

sumDigits x = step x 0
    where step 0 acc = acc
          step y acc = step (y `div` 10) (acc + (y `mod` 10))

main = putStrLn . show . sumDigits $ f 20
