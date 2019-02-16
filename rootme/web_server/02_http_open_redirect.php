<?php
	$site = "index.php";
	$hash = md5($site);
	$url = "http://challenge01.root-me.org/web-serveur/ch52/?url=$site&h=$hash";
	
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_USERAGENT, "MozilaXYZ/1.0");
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_TIMEOUT, 10);
	$output = curl_exec($ch);
	curl_close($ch);

	print($output);

?>