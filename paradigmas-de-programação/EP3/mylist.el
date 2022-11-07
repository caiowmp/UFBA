; Letra a
(defun MYLIST (list-1 list-2)
    (cons list-1 (cons list-2 nil) )
)

; Testes Letra a
 (print (MYLIST 'L' (4 5 6) ) )
 (print (MYLIST '(1 2 3)' (4 5 6) ) )