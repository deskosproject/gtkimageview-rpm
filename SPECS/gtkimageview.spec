Name:           gtkimageview
Version:        1.6.4
Release:        9%{?dist}
Summary:        Simple image viewer widget

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://trac.bjourne.webfactional.com
# To download directly, use this URL:
# Source0:        http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz?format=raw
Source0:        gtkimageview-%{version}.tar.gz
# Fix FTBFS. https://bugzilla.redhat.com/show_bug.cgi?id=1307603
Patch0:         gtkimageview-1.6.4-no-werror.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel >= 2.8.0
BuildRequires:  gtk-doc >= 1.0
BuildRequires:  pkgconfig

%description
GtkImageView is a simple image viewer widget for GTK. It makes writing image
viewing and editing applications easy.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .no-werror


%build
%configure --disable-static
make %{?_smp_mflags}
make %{?_smp_mflags} check


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gtkimageview.pc

%changelog
* Fri Nov 25 2016 Ricardo Arguello <rarguello@deskosproject.org> - 1.6.4-9
- Rebuilt for DeskOS
- don't use -Werror to fix FTBFS (#1307603)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 1.6.4-5
- rebuild for gcc 4.7

* Mon Nov 07 2011 Nils Philippsen <nils@redhat.com> - 1.6.4-4
- rebuild (libpng)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Nils Philippsen <nils@redhat.com> - 1.6.4-2
- don't require gtk-doc but own %%{_datadir}/gtk-doc (#604368, #604169)

* Wed Jun 02 2010 Nils Philippsen <nils@redhat.com> - 1.6.4-1
- version 1.6.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Nils Philippsen <nils@redhat.com> - 1.6.3-1
- version 1.6.3

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 07 2008 Nils Philippsen <nphilipp@redhat.com> - 1.6.1-2
- don't use URL for source since it doesn't download the source directly

* Fri Jul 04 2008 Nils Philippsen <nphilipp@redhat.com> - 1.6.1-1
- version 1.6.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-2
- Autorebuild for GCC 4.3

* Wed Jan 02 2008 Nils Philippsen <nphilipp@redhat.com> - 1.5.0-1
- version 1.5.0
- initial build
