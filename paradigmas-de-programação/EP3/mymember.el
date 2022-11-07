; Letra h
(defun MYMEMBER (word list)
    (setf list-aux list)
    (setf tamanho (- (length list) 1))
    (loop for x from 1 to tamanho do
        (if(= (first list-aux) word)
            (return))

        (if(/= (first list-aux) word)
           (setf list-aux (rest list-aux)))
    )
    (print list-aux)
)

; Testes Letra h
(MYMEMBER 7 '(1 2 3 4 5 6 7 8) )
(MYMEMBER 3 '(1 2 3 4 5 6) )
(MYMEMBER 6 '(1 2 3 4 5 6) ) 
