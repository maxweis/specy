#Maintainer: Maxon Weis <maxrobweis@gmail.com>
pkgname=specy
pkgver=0.8.1
pkgrel=1
pkgdesc="An Arch Linux system command line description output tool"

arch=('any')
url="https://github.com/maxweis/specy"
license=('GPL')
depends=('wmctrl' 'python')
makedepends=('git')
provides=('specy')
md5sums=('SKIP')

source=('specy::git+https://github.com/maxweis/specy')

package() {
	cd "$srcdir/$pkgname"

	install -D -m755 ./specy $pkgdir/usr/bin/specy 
	mkdir -p $pkgdir/home/$USER/.local/share/specy
        chown $USER $pkgdir/home/$USER/.local/share/specy 
	install -o $USER -D -m755 ./ram.py $pkgdir/home/$USER/.local/share/specy 
}
