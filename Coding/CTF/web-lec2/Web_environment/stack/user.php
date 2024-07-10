<?php
// 数据库连接信息
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "sqli_test";

// 创建数据库连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("Error: " . $conn->connect_error);
}


if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $sql = "SELECT * FROM `users` WHERE id = $id";
    echo $sql."<br>";
    $res = mysqli_multi_query($conn, $sql);
    if ($res) {
        do {
            if ($result = mysqli_store_result($conn)) { //获取第一个结果集
                while ($row = mysqli_fetch_row($result)) { //遍历结果集中每条记录
                }
                $result->close(); //关闭一个打开的结果集
            }
        } while (mysqli_more_results($conn) && mysqli_next_result($conn));
    }
}

?>