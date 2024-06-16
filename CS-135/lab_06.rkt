#lang eopl
;Himanshu Rana
;"I pledge my honor that I have abided by the Stevens Honor System"


;; In this lab, we're going to define functions with sets tail
;; recursively
;; To make things simpler we are only going to pass in sets as parameters
;; Do not use make-set for these since make-set is not tail-recursive.

;; Define element? tail recursively
;; Given a set s and an element e, determine whether e in s.
;; If an element is found it should instantly return true otherwise
;; it looks at the rest of the set
;;
;; (element?-tco '(0 1 2 3) 0) => #t
;; (element?-tco '() 'a) => #f
;; (element?-tco '(x y z) 'z) => #t


(define (element?-tco s e)
  (if (null? s)
      #f
      (if (equal? (car s) e)
          #t
          (element?-tco (cdr s) e))))
  


;; Define union-tco (tail recursive union)
;; Given two sets compute the union of the two sets.
;; Order does not matter in this but having duplicate elements is incorrect
;; Add elements to one set while getting rid of elements from the other set
;;
;; (union-tco '(0 1 2 3) '(4 5 6 7)) => '(0 1 2 3 4 5 6 7) (any permutation of this is valid)
;; (union-tco '(1 2 3) '(1 2 3)) => '(1 2 3) (any permutation of this is valid)
;; (union-tco '(1) '()) => '(1)
;; (union-tco '() '(1)) => '(1)

(define (union-tco s t)
  (cond ((null? t) s)
        ((member (car t) s)
         (union-tco s (cdr t)))
        (else (union-tco (cons (car t) s) (cdr t)))))


;; Define intersection-tco-help
;; Given two sets and an empty set return the set of all shared elements
;; Order does not matter in this but having duplicate elements is incorrect
;; rv should be the running set of elements that are being kept
;; 
;; (intersection-tco '(1 3 5) '(1 2 3 4 5)) => '(1 3 5)
;; (intersection-tco '(1 2 3) '(4 5 6)) => '()
;; (intersection-tco '() '(1)) => '()

(define (intersection-tco-help s t rv)
  (if (null? s)
      '()
      (if (member (car s) t)
          (cons (car s) (intersection-tco-help (cdr s) t rv))
          (intersection-tco-help (cdr s) t rv))))

(define (intersection-tco s t)
  (intersection-tco-help s t '()))

;; Define set-difference-tco-help
;; Given two sets remove all the elements from the first set
;; that appear in the second set
;; Order does not matter in this but having duplicate elements is incorrect
;; rv should be the running set of elements that are being kept
;;
;; (set-difference-tco '(1 2 3) '(2 4 6)) => '(1 3)
;; (set-difference-tco '(1 2 3) '()) => '(1 2 3)
;; (set-difference-tco '() '(1 2 3)) => '()

(define (set-difference-tco-help s t rv)
  (cond ((null? s)
         '())
        ((not (member (car s) t))
         (cons (car s) (set-difference-tco-help (cdr s) t rv)))
        (else
         (set-difference-tco-help (cdr s) t rv))))

(define (set-difference-tco s t)
  (set-difference-tco-help s t '()))


;; Final problem: Defining a TCO fibonacci function
;; It takes three arguments, an index and two initializers a, b.
;; The function returns the nth Fibonacci numbers starting at a and b
;; (The general call would be (fib n 0 1)).
;; 
;; (fib 0 2 3) => 2
;; (fib 3 5 8) => 21
;; (fib 12 0 1) => 144?

(define (fib n a b)
  (cond ((zero? n) a)
        (else (fib(- n 1) b (+ a b)))))
