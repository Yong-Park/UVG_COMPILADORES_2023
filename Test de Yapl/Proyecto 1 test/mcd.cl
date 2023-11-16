.data
n: .word 12
n2: .word 36
.text
.globl main
main:
    la $s4, 12($sp)       # Inicializa $s0 con la dirección base de la pila
    lw $a0, n            # Carga el valor de "n" en $a0
    lw $a1, n2           # Carga el valor de "n2" en $a1
    jal MCD              # Llama a la función Maximo Comun Divisor
    add $a0, $v0, $zero  # Coloca el resultado del MCD en $a0
    li $v0, 1            # Cargar el código de la llamada al sistema para imprimir entero
    syscall              # Llama al sistema para imprimir el resultado
    li $v0, 10           # Cargar el código de la llamada al sistema para salir
    syscall              # Llama al sistema para salir

MCD:
    addi $s4, $s4, -12   # Reserva espacio en la pila para tres registros
    sw $ra, 0($s4)       # Guarda $ra en la pila
    sw $s0, 4($s4)       # Guarda $s0 en la pila
    sw $s1, 8($s4)       # Guarda $s1 en la pila
    add $s1, $a0, $zero  # $s1 = $a0 (valor de n)
    add $s2, $a1, $zero  # $s2 = $a1 (valor de n2)
    addi $t1, $zero, 0   # Carga el valor 0 en $t1
    beq $s2, $t1, return # Si $s2 es igual a 0, regresa a return
    add $a0, $zero, $s2  # $a0 = $s2
    div $s1, $s2         # Divide $s1 por $s2
    mfhi $a1             # Coloca el residuo en $a1
    jal MCD              # Llama recursivamente a MCD
    salir:
    lw $ra, 0($s4)       # Recupera $ra desde la pila
    lw $s0, 4($s4)       # Recupera $s0 desde la pila
    lw $s1, 8($s4)       # Recupera $s1 desde la pila
    addi $s4, $s4, 12    # Libera el espacio de la pila
    jr $ra               # Regresa a la dirección de retorno

return:
    add $v0, $zero, $s1  # Establece el resultado (MCD) en $v0
    j salir              # Salta a la etiqueta "salir"


