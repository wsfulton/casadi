classdef swig_ref < handle
    properties (SetAccess = protected)
        ind = libpointer; % a nullpointer
    end
    properties (Constant)
    end
        
    methods
        % constructor
        function h = mx(varargin)
          h.ind = libpointer('int32', 5);
        end

        function convert_input_swig(h)
            libname = 'libcasadi_matlab';
            calllib(libname,'convert_input_swig',h.ind);
        end
        
        % destructor
        function delete(h)
%            ret = calllib('libcasadi','casadi_mx_delete',h.ind);
%            assert(ret==0);
        end
        
        % member functions, overloaded functions and global functions where
        % at lease one of the arguments is a swig_ref goes here
        function plus(h1,h)
            disp('member function')
            disp(h1)
            disp('+')
            disp(h)
        end
    end
    
    methods(Static)
        % constructors and global functions where none of the arguments is a swig_ref goes
        % here. They should be accompanied by .m functions with
        % corresponding names
        function x = one_return_value(h)
            if(nargin<1)
                h = 222;
            end
            
            disp('static function')
            disp(h)
            x = 3;
        end
        
        function no_return_value(h)
            disp('static function')
            disp(h)
        end
        
        function [x,y] = two_return_values(h)
            disp('static function')
            disp(h)
            x = 2;
            y = h;
        end
        
        
    end

end
