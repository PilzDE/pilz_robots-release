Name:           ros-melodic-prbt-moveit-config
Version:        0.5.4
Release:        1%{?dist}
Summary:        ROS prbt_moveit_config package

Group:          Development/Libraries
License:        Apache 2.0
URL:            https://wiki.ros.org/prbt_moveit_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-joint-state-publisher
Requires:       ros-melodic-moveit-fake-controller-manager
Requires:       ros-melodic-moveit-kinematics
Requires:       ros-melodic-moveit-planners-ompl
Requires:       ros-melodic-moveit-ros-move-group
Requires:       ros-melodic-moveit-ros-visualization
Requires:       ros-melodic-moveit-simple-controller-manager
Requires:       ros-melodic-prbt-ikfast-manipulator-plugin
Requires:       ros-melodic-prbt-support
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-rviz
Requires:       ros-melodic-xacro
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roslaunch

%description
An automatically generated package with all the configuration and launch files
for using the prbt with the MoveIt! Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue May 28 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.4-1
- Autogenerated by Bloom

* Thu Apr 25 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.3-1
- Autogenerated by Bloom

* Thu Feb 21 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.2-0
- Autogenerated by Bloom

* Fri Dec 14 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.1-2
- Autogenerated by Bloom

* Fri Dec 14 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.1-1
- Autogenerated by Bloom

* Fri Nov 30 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.1-0
- Autogenerated by Bloom

* Thu Nov 08 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.0-1
- Autogenerated by Bloom

* Wed Nov 07 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.0-0
- Autogenerated by Bloom

* Wed Aug 15 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.3.0-0
- Autogenerated by Bloom

