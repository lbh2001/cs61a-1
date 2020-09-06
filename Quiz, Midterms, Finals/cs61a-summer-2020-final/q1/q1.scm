(define email "aunghtetpaing@berkeley.edu")

;; This question is in two parts, implementing `literature-locator` and
;; `surgery-switch`. See the specifications above each definition
;; for details.
;;
;; NOTE: these parts are unrelated to each other, you can work on
;;    them in any order.

;; Part (a)
;; Implement `literature-locator` which takes in a number `newspaper` and circles
;; all digits of value `8` in the number by returning a list of digits where all the
;; `8` digits are individually placed in a nested list.
;;
;; NOTE 1: Your function should be tail recursive
;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
;;    in a blank
;;
;; To run tests just for this part, run
;;      python3 ok -q a

(define (// numer denom) (floor (/ numer denom)))

;; scm> (literature-locator 12)
;; (1 2)
;; scm> (literature-locator 1881)
;; (1 (8) (8) 1)
;; scm> (literature-locator 0) ; no digits
;; ()
;; scm> (literature-locator 88888888)
;; ((8) (8) (8) (8) (8) (8) (8) (8))
;; scm> (literature-locator 1128651)
;; (1 1 2 (8) 6 5 1)

(define (literature-locator newspaper)
    (define (helper newspaper lis)
        (define current-digit
            (modulo newspaper 10))
        (define value
            (if
                (equal? current-digit 8)
                (list 8)
                current-digit))
        (if (<= newspaper 0)
            lis
            (helper
                (// newspaper 10)
                (cons value lis))))
    (helper newspaper nil))

;; Part (b)
;; The `surgery-switch` operation takes in two infinite streams `aj` and `bt`
;; and returns a new stream containing the non-city elements of each stream,
;; alternating from one stream to the other when encountering the symbol
;; `city`.
;;
;; Note: the symbol `city` should not appear in the final stream.
;;
;;
;; To run tests just for this part, run
;;      python3 ok -q b

;; the following function is defined for testing, and takes the first
;; k elements of a stream `s`, returning them as a list.
(define (take k s)
    (if (zero? k)
        nil
        (cons
            (car s)
            (take (- k 1) (cdr-stream s)))))

;; scm> (define just-city (cons-stream 'city just-city))
;; just-city
;; scm> (define two (cons-stream 1 (cons-stream 'city two)))
;; two
;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'city three))))
;; three
;; scm> (take 10 two)
;; (1 city 1 city 1 city 1 city 1 city)
;; scm> (take 10 three)
;; (x y city x y city x y city x)
;; scm> (take 10 (surgery-switch two three))
;; (1 x y 1 x y 1 x y 1)
;; scm> (take 10 (surgery-switch two just-city))
;; (1 1 1 1 1 1 1 1 1 1)
;; scm> (take 10 (surgery-switch three three))
;; (x y x y x y x y x y)

(define (surgery-switch aj bt)
	(if (not (equal? (car aj) 'city))
		(surgery-switch aj (cdr-stream bt))
		(cons-stream (car aj) (surgery-switch bt (cdr-stream aj)))))


; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `literature-locator` and
; ;; `surgery-switch`. See the specifications above each definition
; ;; for details.
; ;;
; ;; NOTE: these parts are unrelated to each other, you can work on
; ;;    them in any order.

; ;; Part (a)
; ;; Implement `literature-locator` which takes in a number `newspaper` and circles
; ;; all digits of value `8` in the number by returning a list of digits where all the
; ;; `8` digits are individually placed in a nested list.
; ;;
; ;; NOTE 1: Your function should be tail recursive
; ;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
; ;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
; ;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a

; (define (// numer denom) (floor (/ numer denom)))

; ;; scm> (literature-locator 12)
; ;; (1 2)
; ;; scm> (literature-locator 1881)
; ;; (1 (8) (8) 1)
; ;; scm> (literature-locator 0) ; no digits
; ;; ()
; ;; scm> (literature-locator 88888888)
; ;; ((8) (8) (8) (8) (8) (8) (8) (8))
; ;; scm> (literature-locator 1128651)
; ;; (1 1 2 (8) 6 5 1)

; (define (literature-locator newspaper)
;     (define (helper newspaper ______)
;         (define current-digit
;             ______)
;         (define value
;             (if
;                 ______
;                 ______
;                 ______))
;         (if ______
;             ______
;             (helper
;                 ______
;                 (cons value ______))))
;     (helper ______ ______))

; ;; Part (b)
; ;; The `surgery-switch` operation takes in two infinite streams `aj` and `bt`
; ;; and returns a new stream containing the non-city elements of each stream,
; ;; alternating from one stream to the other when encountering the symbol
; ;; `city`.
; ;;
; ;; Note: the symbol `city` should not appear in the final stream.
; ;;
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q b

; ;; the following function is defined for testing, and takes the first
; ;; k elements of a stream `s`, returning them as a list.
; (define (take k s)
;     (if (zero? k)
;         nil
;         (cons
;             (car s)
;             (take (- k 1) (cdr-stream s)))))

; ;; scm> (define just-city (cons-stream 'city just-city))
; ;; just-city
; ;; scm> (define two (cons-stream 1 (cons-stream 'city two)))
; ;; two
; ;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'city three))))
; ;; three
; ;; scm> (take 10 two)
; ;; (1 city 1 city 1 city 1 city 1 city)
; ;; scm> (take 10 three)
; ;; (x y city x y city x y city x)
; ;; scm> (take 10 (surgery-switch two three))
; ;; (1 x y 1 x y 1 x y 1)
; ;; scm> (take 10 (surgery-switch two just-city))
; ;; (1 1 1 1 1 1 1 1 1 1)
; ;; scm> (take 10 (surgery-switch three three))
; ;; (x y x y x y x y x y)

; (define (surgery-switch aj bt)
; 	(if ______
; 		______
; 		(cons-stream ______ ______)))
