# GetWebSiteLinks

爬取站点所有页面的a标签href和script标签的src ， 然后去重 迭代爬取

下面是爬取testphp.vulnweb.com的结果

```
http://testphp.vulnweb.com/product.php?pic=3
http://testphp.vulnweb.com/cart.php
https://www.acunetix.com/blog/articles/prevent-sql-injection-vulnerabilities-in-php-applications/
http://testphp.vulnweb.com/hpp/
http://testphp.vulnweb.com/product.php?pic=7
http://testphp.vulnweb.com/guestbook.php
http://testphp.vulnweb.com/listproducts.php?cat=2
http://testphp.vulnweb.com/Details/network-attached-storage-dlink/1/
http://testphp.vulnweb.com/categories.php
http://testphp.vulnweb.com/artists.php
http://www.eclectasy.com/Fractal-Explorer/index.html
http://testphp.vulnweb.com/artists.php?artist=1
http://testphp.vulnweb.com/showimage.php?file=./pictures/5.jpg
http://testphp.vulnweb.com/showimage.php?file=./pictures/4.jpg
http://testphp.vulnweb.com/listproducts.php?artist=1
http://testphp.vulnweb.com/product.php?pic=1
http://testphp.vulnweb.com/showimage.php?file=./pictures/7.jpg
http://testphp.vulnweb.com/userinfo.php
http://testphp.vulnweb.com/product.php?pic=5
http://testphp.vulnweb.com/listproducts.php?artist=3
http://www.acunetix.com
http://testphp.vulnweb.com/showimage.php?file=./pictures/2.jpg
http://testphp.vulnweb.com/Details/color-printer/3/
http://testphp.vulnweb.com/listproducts.php?artist=2
http://testphp.vulnweb.com/disclaimer.php
http://testphp.vulnweb.com/login.php
http://testphp.vulnweb.com/listproducts.php?cat=1
http://testphp.vulnweb.com/artists.php?artist=2
http://testphp.vulnweb.com/showimage.php?file=./pictures/1.jpg
http://testphp.vulnweb.com/Details/web-camera-a4tech/2/
https://www.acunetix.com/vulnerability-scanner/php-security-scanner/
http://testphp.vulnweb.com/listproducts.php?cat=4
http://testphp.vulnweb.com/privacy.php
http://testphp.vulnweb.com/AJAX/index.php
http://testphp.vulnweb.com/listproducts.php?cat=3
https://www.acunetix.com/vulnerability-scanner/
http://testphp.vulnweb.com/signup.php
http://testphp.vulnweb.com/product.php?pic=2
http://testphp.vulnweb.com/showimage.php?file=./pictures/3.jpg
https://www.acunetix.com/
http://testphp.vulnweb.com/index.php
http://testphp.vulnweb.com?pp=12
http://testphp.vulnweb.com/Mod_Rewrite_Shop/
http://testphp.vulnweb.com/artists.php?artist=3
http://blog.mindedsecurity.com/2009/05/client-side-http-parameter-pollution.html
http://testphp.vulnweb.com/product.php?pic=4

```
