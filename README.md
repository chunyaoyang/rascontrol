# rascontrol
Rascontrol is a Python wrapper for the HEC-RAS controller, described in Chris Goodell's book, 
[*Breaking the HEC-RAS Code*](http://hecrasmodel.blogspot.com/p/book.html), except you get to use Python instead of VBA!
The library can be used to opening, running, and
extracting model results from HEC-RAS models. Rascontrol is *not* recommended for modifying RAS model geometries, instead, 
use the [parserasgeo](https://github.com/mikebannis/parserasgeo) library. The combination of rascontrol and parserasgeo can 
be used for sensitivity studies, Monte Carlo analyses, and real-time predication of floodwater depths when paired with
appropriate rainfall data and hydrology.  


## About This Fork

This is an actively maintained fork of [mikebannis/rascontrol](https://github.com/mikebannis/rascontrol), hosted at [chunyaoyang/rascontrol](https://github.com/chunyaoyang/rascontrol).

### Key Change:
- Modified `get_current_plan()` to return the **filename** of the current plan as a string, instead of a `Plan` object:
  ```python
  def get_current_plan(self):
      """
      Returns name of current plan
      :return: string
      """
      return self.com_rc.CurrentPlanFile()
  ```

This change makes it easier to retrieve the path to the currently selected plan directly, which is useful in workflows that use the plan file for external analysis or postprocessing.

This fork will continue development and welcomes contributions.

## Installation
The appropriate version of HEC-RAS must already be installed to use rascontrol.

    c:\> git clone https://github.com/mikebannis/rascontrol.git
    
    c:\> cd rascontrol
    
    c:\rascontrol> pip install .

## Basic Usage
```python
>>> import rascontrol
>>> rc = rascontrol.RasController(version='506')
>>> rc.open_project('my_model.prj')
>>> rc.run_current_plan()
    
>>> # Get results
>>> profile = rc.get_profiles()[0]
>>> cross_sections = [100, 200, 300]  # Get results for cross sections 100, 200, & 300
>>> wsels = [rc.get_xs(xs).value(profile, rascontrol.WSEL) for xs in cross_sections]
>>> print(wsels)
[5002.3, 5003.5, 5005.1]
```
## Known Issues
close() does not currently appear to be working. This does not typically cause problems during Monte Carlo simulations as rascontrol 
will use any RAS instance that is currently open. Because of this, rascontrol will simply reuse an open model if large numbers 
of simulations are required, versus opening multiple instances of RAS. Make sure you save any open models 
before using rascontrol!
