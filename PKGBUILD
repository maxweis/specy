#Maintainer: Maxon Weis <maxrobweis@gmail.com>

pkgname=specy
pkgver=1.4
pkgrel=1
pkgdesc="An Arch Linux system command line description output tool"

arch=('any')
url="https://github.com/maxweis/specy"
license=('GPL3')
depends=('ncurses')
makedepends=('git')
provides=('specy')
md5sums=('SKIP')

source=('specy::git+https://github.com/maxweis/specy')

package() {
	cd "$srcdir/$pkgname"

	install -D -m755 ./specy $pkgdir/usr/bin/specy 
}
