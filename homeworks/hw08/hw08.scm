(define (rle s)
  (define (helper counter s tracker)
    (cond
      (
        (null? s)
        (cons-stream `(,tracker ,counter) ())
      )
      (
        (= (car s) tracker)
        (helper (+ counter 1) (cdr-stream s) tracker)
      )
      (
        else
        (cons-stream
          `(,tracker ,counter)
          (helper
            1
            (cdr-stream s)
            (car s)
          )
        )
      )
    )
  )
  (if
    (null? s)
    `()
    (helper 0 s (car s))
  )
)



(define (group-by-nondecreasing s)
  (define (helper s lis)
    (cond
      (
        (null? s)
        (cons-stream lis nil)
      )
      (
        (null? (cdr-stream s))
        (helper nil (append lis (list (car s))))
      )
      (
        (<= (car s) (car (cdr-stream s)))
        (helper (cdr-stream s) (append lis (list (car s))))
      )
      (
        else
        (cons-stream
          (append lis (list (car s)))
          (helper
            (cdr-stream s)
            nil
          )
        )
      )
    )
  )
  (helper s nil)
)

(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
