Name:           clearwater-radius-auth
Summary:        Package enabling RADIUS authentication on Clearwater nodes
BuildArch:      noarch
BuildRequires:  python2-devel python-virtualenv
Requires:       libpam-radius-auth libnss-ato

%include %{rootdir}/build-infra/cw-rpm.spec.inc

%description
Package enabling RADIUS authentication on Clearwater nodes

%install
. %{rootdir}/build-infra/cw-rpm-utils %{rootdir} %{buildroot}
setup_buildroot
install_to_buildroot < %{rootdir}/debian/clearwater-radius-auth.install
build_files_list > clearwater-radius-auth.files

%post
/usr/share/clearwater/infrastructure/install/clearwater-radius-auth.postinst

%preun
/usr/share/clearwater/infrastructure/install/clearwater-radius-auth.prerm

%files -f clearwater-radius-auth.files
