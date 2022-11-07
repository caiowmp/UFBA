; Letra f
(defun MYLAST (list)
    (setf list-aux nil )
    (loop for x from 1 to (- (length list) 1) do
          (setf list (rest list) )
    )
    (print list)
)

; Testes Letra f
 (MYLAST '(1 2 3 4 5 6 7 8 9) )
 (MYLAST '(1 2 3 4 5 6 7) )
 (MYLAST '(1 2 3 4 5) )