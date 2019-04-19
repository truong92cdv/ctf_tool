<?php
	
	$num = ceil(exp(pi()));
	$code = "ceil(exp(pi()))";
	while (true) 
	{
		if (chr($num) === '.')
		{
			// echo strlen($code);
			die('chr('.$code.')');
		}
		$code = "ceil(strrev(sin(" . $code . ")))";
		$num = ceil(strrev(sin($num)));
	}
?>