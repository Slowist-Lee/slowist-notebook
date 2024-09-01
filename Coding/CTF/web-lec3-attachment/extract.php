<?php
$dragon = "pite174";
if ($_GET['doragonn']) extract($_GET['doragonn']);
var_dump($dragon);
highlight_file(__FILE__);
// Try: ?doragonn[dragon]=zero
?>