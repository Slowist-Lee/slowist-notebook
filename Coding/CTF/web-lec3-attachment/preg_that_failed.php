<?php
// var_dump(ini_get('pcre.backtrack_limit'));
$input = file_get_contents($_FILES["file"]["tmp_name"]);
// var_dump($input);

function is_php($data){  
    return preg_match('/<\?.*[(`;?>].*/is', $data);  
}

if(!is_php($input)) {
    echo "Booooooom! You've got me.";
    file_put_contents("shell.php", $input);
}
echo "^_^";
// Tips: use var_dump() to find out the actual return value of preg_match()
?>