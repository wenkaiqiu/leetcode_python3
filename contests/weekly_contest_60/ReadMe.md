# Weekly Contest 60

## 733. Flood Fill

An `image` is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the `newColor`.

At the end, return the modified image.

**Example 1:**

**Input:**
```
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
```
**Output:**
```
[[2,2,2],[2,2,0],[2,0,1]]
```
**Explanation:**
```
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
```

**Note:**
- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and `0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and newColor will be an integer in `[0, 65535]`.

## 734. Sentence Similarity

Given two sentences `words1`, `words2` (each represented as an array of strings), and a list of similar word pairs `pairs`, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are `pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]`.

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are **not** necessarily similar.

Also, a word is always similar with itself. For example, the sentences `words1 = ["great"], words2 = ["great"], pairs = []` are similar, even though there are no specified similar word pairs.

**Note:**

- The length of `words1` and `words2` will not exceed `1000`.
- The length of `pairs` will not exceed `2000`.
- The length of each `pairs[i]` will be `2`.
- The length of each `words[i]` and `pairs[i][j]` will be in the range `[1, 20]`.

## 735. Asteroid Collision
We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.

**Example 1:**

**Input:**
```
asteroids = [5, 10, -5]
```
**Output:**
```
[5, 10]
```
**Explanation:**
```
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
```

**Example 2:**

**Input:**
```
asteroids = [8, -8]
```
**Output:**
```
[]
```
**Explanation:**
```
The 8 and -8 collide exploding each other.
```

**Example 3:**

**Input:**
```
asteroids = [10, 2, -5]
```
**Output:**
```
[10]
```
**Explanation:**
```
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
```
**Note:**

- The length of `asteroids` will be at most `10000`.
- Each asteroid will be a non-zero integer in the range `[-1000, 1000]`.

## 736. Parse Lisp Expression

You are given a string `expression` representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

- An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
- A let-expression takes the form `(let v1 e1 v2 e2 ... vn en expr)`, where `let` is always the string `"let"`, then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable `v1` is assigned the value of the expression `e1`, the second variable `v2` is assigned the value of the expression `e2`, and so on **sequentially**; and then the value of this let-expression is the value of the expression expr.
- An add-expression takes the form `(add e1 e2)` where `add` is always the string `"add"`, there are always two expressions `e1, e2`, and this expression evaluates to the addition of the evaluation of `e1` and the evaluation of `e2`.
- A mult-expression takes the form `(mult e1 e2)` where `mult` is always the string `"mult"`, there are always two expressions `e1, e2`, and this expression evaluates to the multiplication of the evaluation of `e1` and the evaluation of `e2`.
- For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
- Finally, there is the concept of scope. When an expression of a variable name is evaluated, **within the context of that evaluation**, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.
Evaluation Examples:
>**Input:** (add 1 2)
>
>**Output:** 3
>
>**Input:** (mult 3 (add 2 3))
>
>**Output:** 15
>
>**Input:** (let x 2 (mult x 5))
>
>**Output:** 10
>
>**Input:** (let x 2 (mult x (let x 3 y 4 (add x y))))
>
>**Output:** 14
>
>**Explanation:** In the expression (add x y), when checking for the value of the variable x,
>we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
>Since x = 3 is found first, the value of x is 3.

>**Input:** (let x 3 x 2 x)
>
>**Output:** 2
>
>**Explanation:** Assignment in let statements is processed sequentially.
>
>**Input:** (let x 1 y 2 x (add x y) (add x y))
>
>**Output:** 5
>
>**Explanation:** The first (add x y) evaluates as 3, and is assigned to x.
>The second (add x y) evaluates as 3+2 = 5.
>
>**Input:** (let x 2 (add (let x 3 (let x 4 x)) x))
>
>**Output:** 6
>
>**Explanation:** Even though (let x 4 x) has a deeper scope, it is outside the context of the final x in the add-expression.  That final x will equal 2.
>
>**Input:** (let a1 3 b2 (add a1 1) b2)
>
>**Output:** 4
>
>**Explanation:** Variable names can contain digits after the first character.

**Note:**

- The given string `expression` is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
- The length of `expression` is at most 2000. (It is also non-empty, as that would not be a legal expression.)
- The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.