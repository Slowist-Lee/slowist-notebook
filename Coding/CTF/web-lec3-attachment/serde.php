<?php
      class Name{
        private $username = 'nonono';
        private $password = 'yesyes';
    }
    $tmp = new Name('admin',100);
    var_dump(base64_encode(serialize($tmp)));
    //Tzo0OiJOYW1lIjoyOntzOjE0OiIATmFtZQB1c2VybmFtZSI7czo2OiJub25vbm8iO3M6MTQ6IgBOYW1lAHBhc3N3b3JkIjtzOjY6Inllc3llcyI7fQ==

    // What if we change private to publice/protected ?


    class Exp{
      public $a = '123';
    }
    $tmp = new Exp;
    //$b = serialize($tmp);


    $ser = 'O:3:"Exp":1:{s:1:"a";S:4:"\41\42\43\44";}';
    $unser = unserialize($ser);
    print_r($unser);
?>
