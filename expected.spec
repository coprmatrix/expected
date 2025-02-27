#
# spec file for package expected
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define __builder ninja
Name:           expected
Version:        1.0.0
Release:        0
Summary:        C++11/14/17 std::expected with functional-style extensions
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        CC0-1.0
URL:            https://github.com/TartanLlama/expected
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch0:         expected-cmake.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  (ninja or ninja-build)
BuildArch:      noarch

%description
Single header implementation of std::expected with functional-style extensions.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version} , cmake(tl-expected)

%description devel
Header-only %{summary}.

%prep
%autosetup

%build
%cmake \
 -DCMAKE_BUILD_TYPE=Release \
 -DEXPECTED_BUILD_TESTS=OFF \
 -DEXPECTED_BUILD_PACKAGE=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc README.md
%license COPYING
%{_includedir}/tl
%{_datadir}/cmake/tl-%{name}

%changelog

