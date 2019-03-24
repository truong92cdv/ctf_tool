<?php

if(";" === preg_replace("/[^\W]+\((?R)?\)/", "", $_GET['code']))
{
	if(preg_match("/_|m|info|get/i",$_GET['code']))
	{
		die('Hi DoubleVKay, not easy, right?<audio controls autoplay loop hidden><source src="assets/nhac.mp3" type="audio/mpeg"></audio>');
	}
	else
	{
		eval($_GET['code']);
	}
}
else
{
	show_source(__FILE__);
}

?>
