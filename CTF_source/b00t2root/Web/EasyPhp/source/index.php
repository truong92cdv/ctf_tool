 <?php
include "flag.php";
highlight_file(__FILE__);
error_reporting(0);
$str1 = $_GET['1'];

if(isset($_GET['1'])){
    if($str1 == md5($str1)){
        echo $flag1;
    }
    else{
        die();
    }
}
else{
    die();   
}

$str2 = $_GET['2'];
$str3 = $_GET['3'];

if(isset($_GET['2']) && isset($_GET['3'])){
    if($str2 !== $str3){
        if(hash('md5', $salt . $str2) == hash('md5', $salt . $str3)){
            echo $flag2;
        }
        else{
            die();
        }
    }
    else{
        die();
    }
}
else{
    die();   
}
?>
<?php

class Secrets {
    var $temp;
    var $flag;
}
   
if (isset($_GET['4'])) {
    $str4 = $_GET['4'];

    if(get_magic_quotes_gpc()){
        $str4=stripslashes($str4);
    }
   
    $res = unserialize($str4);
   
    if ($res) {
    $res->flag=$flag3;
        if ($res->flag === $res->temp)
            echo $res->flag;
        else
            die();
    }
    else die();
}

?> 