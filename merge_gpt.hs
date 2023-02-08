haskel for merge sort
 §§ --- Haskell/merge_sort.hs
 §§ 1000
+merge :: (Ord a) => [a] -> [a] -> [a]
+merge xs [] = xs
+merge [] ys = ys
+merge (x:xs) (y:ys) 
+    | x <= y = x : merge xs (y:ys)
+    | otherwise = y : merge (x:xs) ys
+
+merge_sort :: (Ord a) => [a] -> [a]
+merge_sort [] = []
+merge_sort [x] = [x]
+merge_sort xs = 
+    let 
+        l = length xs
+        (xs1, xs2) = splitAt (div l 2) xs
+    in
+        merge (merge_sort xs1) (merge_sort xs2)
+
+main = do
+    let xs = [1, 2, 6, 8, 4, 0, 10, 5, 7, 3, 9]
+    print $ merge_sort xs
