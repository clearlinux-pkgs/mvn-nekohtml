#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-nekohtml
Version  : 1.9.6.2
Release  : 3
URL      : https://repo1.maven.org/maven2/nekohtml/nekohtml/1.9.6.2/nekohtml-1.9.6.2.jar
Source0  : https://repo1.maven.org/maven2/nekohtml/nekohtml/1.9.6.2/nekohtml-1.9.6.2.jar
Source1  : https://repo1.maven.org/maven2/nekohtml/nekohtml/1.9.6.2/nekohtml-1.9.6.2.pom
Source2  : https://repo1.maven.org/maven2/net/sourceforge/nekohtml/nekohtml/1.9.22/nekohtml-1.9.22.jar
Source3  : https://repo1.maven.org/maven2/net/sourceforge/nekohtml/nekohtml/1.9.22/nekohtml-1.9.22.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-nekohtml-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-nekohtml package.
Group: Data

%description data
data components for the mvn-nekohtml package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/nekohtml/nekohtml/1.9.6.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/nekohtml/nekohtml/1.9.6.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/nekohtml/nekohtml/1.9.6.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/nekohtml/nekohtml/1.9.6.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/nekohtml/nekohtml/1.9.22
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/nekohtml/nekohtml/1.9.22

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/nekohtml/nekohtml/1.9.22
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/sourceforge/nekohtml/nekohtml/1.9.22


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/nekohtml/nekohtml/1.9.6.2/nekohtml-1.9.6.2.jar
/usr/share/java/.m2/repository/nekohtml/nekohtml/1.9.6.2/nekohtml-1.9.6.2.pom
/usr/share/java/.m2/repository/net/sourceforge/nekohtml/nekohtml/1.9.22/nekohtml-1.9.22.jar
/usr/share/java/.m2/repository/net/sourceforge/nekohtml/nekohtml/1.9.22/nekohtml-1.9.22.pom
