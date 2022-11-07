; Letra d
(defun MYNTHCDR (n list-1)
    (setf list-aux list-1)
    (if (>= n (length list-1) ) (print nil) )
    (if (< n (length list-1) ) (loop for x from 1 to n do
                                  (setf list-aux (rest list-aux) )
                                ) )
    (if (< n (length list-1) ) (print list-aux) )
)

; Testes Letra d
 (MYNTHCDR 3 '(1 2 3 4 5 6 7 8) )  
 (MYNTHCDR 6 '(1 2 3 4 5 6) )
 (MYNTHCDR 0 '(1 2 3 4 5 6) )