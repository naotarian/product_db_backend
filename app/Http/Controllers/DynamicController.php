<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;


class DynamicController extends Controller
{
    public function test() {
        $path =  app_path() . "/Library/Python/text_extract.py 2>&1";
        $command="python3 " . $path;
        exec($command, $output, $return);
    }
}
