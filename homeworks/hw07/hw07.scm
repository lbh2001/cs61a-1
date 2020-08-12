(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (sign num)
  'YOUR-CODE-HERE
  (cond
    ((= num 0) 0)
    ((< num 0) -1)
    ((> num 0) 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond
    ((= y 1) x)
    ((even? y) (square (pow x (quotient y 2))))
    ((odd? y) (* (square (pow x (quotient y 2))) x))
  )
)


(define (unique s)
  'YOUR-CODE-HERE
  (define (helper)
    (define first (car s))
    (define rest (cdr s))
    (define filtered (filter (lambda (x) (not (eq? x first))) rest))
    (cons first
      (if (not (null? filtered))
        (unique filtered)
        nil
        )
        )
  )
  (if (null? s)
    nil
    (helper)
  )
)


(define (replicate x n)
  'YOUR-CODE-HERE
  (define (helper list_sofar l)
    (if (= l 0)
      list_sofar
      (helper (append list_sofar (list x)) (- l 1))
    )
  )
  (helper () n)
)


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0)
    start
    (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (helper seq total)
    (if (= seq 0)
      total
      (helper (- seq 1) (combiner total (term seq)))
    )
  )
  (helper n start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  `(map
      (lambda (,var) ,map-expr)
      (filter (lambda (,var) ,filter-expr) ,lst)
    )
)
