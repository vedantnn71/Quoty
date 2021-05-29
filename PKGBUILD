# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=Quoty
pkgver=0.1
pkgrel=1
epoch=
pkgdesc="Python script to get random motivational quotes"
arch=("x86_64")
url="https://gitlab.com/vedantnn7/quoty"
license=('GPL')
groups=()
depends=('python3')
makedepends=('python3')
checkdepends=()
optdepends=()
provides=('quoty')
conflicts=('quoty')
replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname.tar.gz")
noextract=()
md5sums=()
validpgpkeys=()

prepare() {
	cd "$pkgname"
	echo "Getting Ready ..."
}	
build() {
	cd "$pkgname"
	cp -r ./dist/quoty /opt/
}
package() {
	echo "Done ... \n run python /opt/quoty/quoty to run it"
}
