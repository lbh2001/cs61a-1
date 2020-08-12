;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (spiral len)
  (cond
    ((> len 0)
    (forward len)
    (right 90)
    (spiral (- len 5))
    )
  )
)

(define (reverse_spiral)
  (penup)
  (left 90)
  (forward 50)
  (left 90)
  (forward 150)
  (pendown)
)

(define (leaves num)
  (cond
    ((> num 0)
      (forward 100)
      (spiral 100)
      (reverse_spiral)
      (left 139)
      (leaves (- num 1))
    )
  )
)

(define (mytree)
  (left 161)
  (leaves 8)
  (right 13)
  (forward 500)
)

(define (draw)
  (mytree)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
