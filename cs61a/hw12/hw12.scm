(define (find s predicate)
  (cond
  	((null? s) #f)
  	((predicate (car s)) (car s))
  	(else (find (cdr-stream s) predicate)
  		)
  	)

  	)

(define (scale-stream s k)
  (if (null? s) 
  	nil
  	(cons-stream (* k (car s)) (scale-stream (cdr-stream s) k) )
  	)
)

(define (has-cycle s)
	(define (helper orig new)
	(cond 
  		((null? new) #f)
  		((eq? orig new) #t)
  		(else (helper orig (cdr-stream new)))
		)
  	)
  	(helper s (cdr-stream s))
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
