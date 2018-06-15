Name:       speexdsp
Summary:    Software DSP library
Version:    1.2.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.speex.org/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).


%package devel
Summary:    Development package for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static --enable-fixed-point
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -f $RPM_BUILD_ROOT%{_docdir}/speexdsp/manual.pdf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libspeexdsp.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS
%{_includedir}/speex/speex_echo.h
%{_includedir}/speex/speex_jitter.h
%{_includedir}/speex/speex_preprocess.h
%{_includedir}/speex/speex_resampler.h
%{_includedir}/speex/speexdsp_config_types.h
%{_includedir}/speex/speexdsp_types.h
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so
