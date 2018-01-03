;; Extra Scheme Questions ;;

; Q5
(define (square x) (* x x))

(define (pow b n)
  (cond
  	((= n 0) 1)
    ((= n 1) b)
    ((even? n) (square (pow b (quotient n 2))))
    ((odd? n) (* b (pow b (- n 1))))
    )
)

; Q6
(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil))))
)

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q8
(define (remove item lst)
  (cond
		((null? lst) nil)
		((null? (cdr lst))
			(if (= (car lst) item)
				nil
				(cons (car lst) nil)
			)
		)
		((= (car lst) item)
			(remove item (cdr lst))
			)
		(else (cons (car lst) (remove item (cdr lst))))
		)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond 
  	((= a 0) b)
  	((= b 0) a)
  	((= a b) a)
  	((= (remainder (max a b) (min a b)) 0) (min a b))
  	(else (gcd (min a b) (remainder (max a b) (min a b))))

  	)
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q10
(define (no-repeats s)
  (if (null? s) nil
  (cons (car s) (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s))))
  )
)

; Q11
(define (substitute s old new)
  (cond 
  	((null? s) ())
  	((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
  	((eq? (car s) old) (cons new (substitute (cdr s) old new)))
  	(else (cons (car s) (substitute (cdr s) old new)))
  	)
)

; Q12
(define (sub-all s olds news)
  (cond 
  	((null? olds) s)
  	(else (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
  	)
)