#! /bin/sh

cat <<eof
Content-type: text/html

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
	<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
	<meta name="author" content="SCG" />
	<meta name="keywords" content="concurrent programming" />
	<meta name="description" content="Petri Net Examples"/>
	<meta name="robots" content="all" />
	<title>PetitPetri examples</title>
	<link href="../content.css" rel="stylesheet" type="text/css">
</head>
<body>
<div id="header">
	<h1>Petit Petri::Petri Net Examples</h1>
</div>
<div id="breadcrumb">
	<a href="http://www.unibe.ch/">unibe</a>
	<a href="http://www.iam.unibe.ch/en">iam</a>
	<a href="http://www.iam.unibe.ch/~scg/index.html">scg</a>
	<a href="http://www.iam.unibe.ch/~scg/teaching.html">teaching</a>
	<a href="http://www.iam.unibe.ch/~scg/Teaching/CP/index.html">cp</a>
	<a href="../index.html">petri nets</a>
	<a href="index.cgi">examples</a>
</div>
<div id="menu">
<!-- -->
</div>
<div id="content">
<h1>Petri net examples</h1>
<p>
eof

sl="http://www.squeakland.org/project.jsp"

for pr in *.pr
do
	url="http://www.iam.unibe.ch/~scg/Teaching/CP/PetriNets/Squeaklets/$pr"
	gif=`echo ${pr} | sed 's/\..*/.gif/'`
	echo "<a target="_blank" href=\"${sl}?${url}\"><img src=\"${gif}\"></a>"
	# echo "<a href=\"${sl}?${url}\">${pr}</a>"
done

cat <<eof
</p>
<!-- Original version 2005-11-13 -->
<div id=lastModified>$Id: index.cgi 24473 2009-01-29 12:13:55Z oscar $ &#8212;&nbsp; <a href="http://www.iam.unibe.ch/~oscar/">omn</a></div>
</div>
</body>
</html>
eof
