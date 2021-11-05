#lang rosette/safe
(require rosette/lib/synthax)

(define-symbolic y integer?)
(define (mul2_?? x)
  (* x (??)))

(mul2_?? 3)
(equal? (mul2_?? y) (mul2_?? y))

(define sol
  (synthesize
   #:forall (list y)
   #:guarantee (assert (equal? (mul2_?? y) (* y 2)))))

sol
(print-forms sol)

(define-grammar (intfast y)
  [expr
   (choose y (??)
           ((int_op) (expr) (expr)))]
  [int_op
   (choose * + - /)])

(define (mul2_intfast x)
  (intfast x #:depth 2))

(define sol2
  (synthesize
   #:forall (list y)
   #:guarantee (assert (equal? (mul2_intfast y) (* 2 (* 5 (* y 2)))))))
(print-forms sol2)

; Specifies a grammar of signed and unsigned
; comparisons of intfast expressions.
(define-grammar (intcmp y)
  [cmp
   (choose
    ((op) (intfast y) (intfast y))
    (and (cmp) (cmp))
    (or (cmp) (cmp))
    (not (cmp)))]
  [op
   (choose = < <= > >=)])

(current-grammar-depth 2)

(generate-forms sol)

(define-grammar (fast-int x y)
  [expr
   (choose x y (?? integer?)
           ((int_op) (expr) (expr)))]
  [int_op
   (choose * + - /)])

; midpoint calculation
; this sketch describes the space of all expressions from the intfast grammar with parse trees on depth at most 2
(define (intmid-fast lo hi)
  (fast-int lo hi #:depth 5))

(define (check-mid impl lo hi)  ; Assuming that
  (assume (<= 0 lo))            ; 0 ≤ lo and
  (assume (<= lo hi))           ; lo ≤ hi,
  (define mi (impl lo hi))      ; and letting mi = impl(lo, hi) and
  (define diff                  ; diff = (hi - mi) - (mi - lo),
    (bvsub (- hi mi)
           (- mi lo)))          ; we require that
  (assert (<= lo mi))           ; lo ≤ mi,
  (assert (<= mi hi))           ; mi ≤ hi,
  (assert (<= 0 diff))          ; 0 ≤ diff, and
  (assert (<= diff 1)))         ; diff ≤ 1.

(define-symbolic l h integer?)
(define sol3
  (synthesize
   #:forall (list l h)
   #:guarantee (check-mid intmid-fast l h)))
;sol3
;(print-forms sol3)

;The synthesis query takes the form (synthesize #:forall input #:guarantee expr),
;where input lists the symbolic constants that represent inputs to a sketched program,
;and expr gives the correctness specification for the sketch.
;The solver searches for a binding from the hole (i.e., non-input) constants to values such
;that expr satisfies its assertions on all legal inputs.
;Passing this binding to print-forms converts it to a syntactic representation of the
;completed sketch.
(clear-vc!)
(define-symbolic p boolean?)
(define-grammar (boolfast p)
  [expr
   (choose p (?? boolean?)
           ((bool_op) (expr) (expr))
           (not (expr)))]
  [bool_op (choose && || xor => <=>)])

(define (bfunc p) (boolfast p #:depth 3))
(define-symbolic q boolean?)
(define sol4
  (synthesize
   #:forall (list q p)
   #:guarantee (assert (equal? (bfunc q) (&& q (|| p q))))))
;sol4
;get all solutions
;make it do what my tool was doing (print multiple functions, sat unsat valid etc, 
;format string in lean format
;more systematic and generalized
;document code, here's what I want to do and here's how I do it. for each thing.
;different types of problems, filling in holes
;put in git repo
(print-forms sol4)
(generate-forms sol4)


