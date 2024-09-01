<?php
// 数据库连接信息
// $servername = "localhost";
// $username = "root";
// $password = "lx051607";
// $dbname = "sqli_test";
$servername = "localhost";
$username = "root";
$password = "lx051607";
$dbname = "sqli_test";
// 创建数据库连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("Error: " . $conn->connect_error);
}

$charId = $_GET['id'];
# echo $charId.'<br>';
// 查询数据库
if ($charId > 0) {
    $sql = "SELECT * FROM `chars` WHERE id = $charId";
    echo $sql."<br>";
    $result = $conn->query($sql);
    
    if (!$result) {
        echo $conn->error."<br>";
    }

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        echo "<p>ID: " . $user['id'] . "</p>";
        echo "<p>Name: " . $user['name'] . "</p>";
    } else {
        echo "<p>Not Found</p>";
    }
} else {
    echo "<p>Invalid ID</p>";
}

// 关闭数据库连接
$conn->close();

?>
