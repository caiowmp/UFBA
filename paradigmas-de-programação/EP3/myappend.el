; Letra b
(defun MYAPPEND (list-1 list-2)
    (cons  (first list-1) (cons (first(rest list-1) ) (cons (first(rest (rest list-1) ) ) list-2) ) )
)

;Testes Letra b
 (print (MYAPPEND '(1 2 3)' (4 5 6 8 9) ) )
 (print (MYAPPEND '(1 2 3)' (4 5 6) ) )