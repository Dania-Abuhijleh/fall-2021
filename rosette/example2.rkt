#lang rosette/safe
(require rosette/lib/angelic    ; provides `choose*`
         rosette/lib/destruct)  ; provides `destruct`
; Tell Rosette we really do want to use integers.
(current-bitwidth #f)

; Syntax for our simple DSL 
(struct len (l) #:transparent)
(struct app (left right) #:transparent)
(struct rev (l) #:transparent)

; Interpreter for our DSL.
; We just recurse on the program's syntax using pattern matching.
(define (interpret p)
  (destruct p
    [(len a) (if (null? (interpret a)) 0 (+ 1 (len (list-tail (interpret a) 1))))]
    [(app a b) (if (null? (interpret a)) (interpret b) (cons (list-ref (interpret a) 0) (app (list-tail (interpret a) 1) (interpret b))))]
    [(rev a) (if (null? (interpret a)) null (app (rev (list-tail (interpret a) 1)) (list (list-ref (interpret a) 0))))]
    [_ p]))

(define-symbolic x list?)

; This does NOT work because list is not a solvable type
(synthesize
  #:forall (list x)
  #:guarantee (assert (= (interpret (len x)) 0)))
