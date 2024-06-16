#lang eopl
;;Himanshu Rana
;;"I pledge my honor that I have abided by the Stevens Honor System"
;; Some basic logic operators, defined in terms of Scheme's built-in 
;; and,or,not 

;; Remember that Scheme uses prefix notation, so "x ^ y" is written "(and x y)"


;; Define (nand p q) which follows this truth table:
;; ((#t #t) #f)
;; ((#t #f) #t)
;; ((#f #t) #t)
;; ((#f #f) #t)


;; Type signature: (nand boolean boolean) -> boolean

(define (nand p q)
(or
 (and p(not q))
 (and (not p) q)
 (and (not p) (not q))))

             
          
;; Define if->then, it has the truth table
;; ((#t #t) #t)
;; ((#t #f) #f)
;; ((#f #t) #t)
;; ((#f #f) #t)

;; Type signature: (if->then boolean boolean) -> boolean

(define (if->then p q)
  (or
  (and (not p) q)
  (and p q)
  (and (not p) (not q))))



;; Define (xor p q) exclusive or
;; ((#t #t) #f)
;; ((#t #f) #t)
;; ((#f #t) #t)
;; ((#f #f) #f)

;; Type signature: (xor boolean boolean) -> boolean

(define (xor p q)
  (or
  (and p (not q))
  (and (not p) q)
  ))

;; Define (nor p q)
;; ((#t #t) #f)
;; ((#t #f) #f)
;; ((#f #t) #f)
;; ((#f #f) #t)

;; Type signature: (nor boolean boolean) -> boolean
(define (nor p q)
  (not (or p q)
  ))


;; Define (3majority p q r)
;; Create a function that returns #t when a majority of its three
;; arguments are #t
;; 
;; ((#t #t #t) #t)
;; ((#t #t #f) #t)
;; ((#t #f #t) #t)
;; ((#t #f #f) #f)
;; ((#f #t #t) #t)
;; ((#f #t #f) #f)
;; ((#f #f #t) #f)
;; ((#f #f #f) #f)

;; Type signature: (3majority boolean boolean boolean) -> boolean
(define (3majority p q r)
  (or
  (and p q r )
  (and p q)
  (and p r)
  (and q r)))

  

;; Define (isosceles p q r)
;; Create a function that returns #t when exactly two of its
;; arguments are #t

;; ((#t #t #t) #f)
;; ((#t #t #f) #t)
;; ((#t #f #t) #t)
;; ((#t #f #f) #f)
;; ((#f #t #t) #t)
;; ((#f #t #f) #f)
;; ((#f #f #t) #f)
;; ((#f #f #f) #f)

(define (isosceles p q r)
  (or
  (and p (not q) r)
  (and (not p) q r)
  (and p q (not r)
  )))

;; Define (commutative? operator)
;; Returns #t iff the operator is commutative
;; i.e., in all cases (operator p q) is the same as (operator q p)
;; E.g. (commutative? nand) is #t since (nand p q) = (nand q p) in
;; all cases

;; Type signature: (commutative? operator) -> boolean
;; Where operator's type signature is (operator boolean boolean) -> boolean
(define (commutative? operator)
  (and
  (equal? (operator #t #t) (operator #t #t))
  (equal? (operator #t #f) (operator #f #t))
  (equal? (operator #f #t) (operator #t #f))
  (equal? (operator #f #f) (operator #f #f))))
  


;; January 2018
;; Samuel Kraus and Edward Minnix
;; Stevens Institute of Technology
;; CS 135  Discrete Structures
