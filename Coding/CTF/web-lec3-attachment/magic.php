<?php
class test{
    public $varr1="abc";
    public $varr2="123";
    public function display(){
        echo $this->varr1."\n";
    }
    public function __construct(){
        echo "__construct called\n";
    }
    public function __destruct(){
        echo "__destruct called\n";
    }
    public function __toString(){
        return "__toString called\n";
    }
    public function __sleep(){
        echo "__sleep called\n";
        return array('varr1','varr2');
    }
    public function __wakeup(){
        echo "__wakeup called\n";
    }
    public function __invoke(){
        echo "__invoke called\n";
    }

}

$obj = new test();  //实例化对象，调用__construct()方法，输出__construct
$obj->display();   //display()方法，输出"abc"
echo $obj;    //obj对象被当做字符串输出，调用__toString()方法，输出__toString
$s = serialize($obj);  //obj对象被序列化，调用__sleep()方法，输出__sleep
echo unserialize($s);  //$s首先会被反序列化，会调用__wakeup()方法，被反序列化出来的对象又被当做字符串，就会调用__toString()方法。

$obj();//将对象调用为函数时触发

// 脚本结束又会调用__destruct()方法，输出__destruct


/*结果展示
__construct called
abc
__toString called
__sleep called
__wakeup called
__toString called
__destruct called
__invoke called
__destruct called
 */
?>