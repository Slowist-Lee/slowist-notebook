<?php
// serde_challenge.php

class Exp {
    public $enter;
    public $secret;
}

$o = unserialize($_GET['guess']);

if ($o) {
    $o->secret = "AAA{php_unserialize}";
    if ($o->secret === $o->enter)
        echo "Congratulation! Here is my secret: ".$o->secret;
    else
        echo "Oh no... You can't fool me";
}
else echo "are you trolling?";
// string(45) "O:3:"Exp":2:{s:5:"enter";N;s:6:"secret";R:2;}"
// Congratulation! Here is my secret: AAA{php_unserialize}
?>

